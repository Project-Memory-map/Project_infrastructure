(() => {
  const forms = document.querySelectorAll("form[data-endpoint]");

  function validate(data) {
    if (data.password !== undefined && data.password_confirm !== undefined && data.password !== data.password_confirm) {
      return "Mật khẩu nhập lại không khớp";
    }
    if (data.new_password !== undefined && data.password_confirm !== undefined && data.new_password !== data.password_confirm) {
      return "Mật khẩu nhập lại không khớp";
    }
    return "";
  }

  function buildPayload(form) {
    if (form.enctype === "multipart/form-data") {
      return { formData: new FormData(form) };
    }
    const data = UI.formToJson(form);
    delete data.password_confirm;
    const token = new URLSearchParams(window.location.search).get("token");
    if (form.dataset.withToken !== undefined && token) {
      data.token = token;
    }
    return { body: data };
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const message = form.querySelector(".form-message");
    const error = validate(UI.formToJson(form));
    if (error) {
      UI.showMessage(message, error);
      return;
    }

    UI.setBusy(form, true);
    UI.showMessage(message, "");
    try {
      const method = (form.dataset.method || "post").toLowerCase();
      const result = await Api[method](form.dataset.endpoint, buildPayload(form));
      if (result && result.access_token) {
        Api.setToken(result.access_token);
      }
      if (form.dataset.redirect) {
        window.location.href = form.dataset.redirect;
        return;
      }
      UI.showMessage(message, form.dataset.success || "Đã lưu thành công", "success");
      form.dispatchEvent(new CustomEvent("accounts:saved", { detail: result }));
    } catch (requestError) {
      UI.showMessage(message, requestError.message);
    } finally {
      UI.setBusy(form, false);
    }
  }

  forms.forEach((form) => form.addEventListener("submit", handleSubmit));
})();
