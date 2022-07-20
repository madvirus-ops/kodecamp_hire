const togglePassword = document.querySelector('#togglePassword');
  const password = document.querySelector('#exampleInputPassword1');
 
  togglePassword.addEventListener('click', function (e) {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.classList.toggle('bi bi-eye-slash-fill');
});
const togglePassword2 = document.querySelector('#togglePassword2');
const passwordSecond = document.querySelector('#exampleInputPassword2');

togglePassword2.addEventListener('click', function (e) {
    const type = passwordSecond.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordSecond.setAttribute('type', type);
    this.classList.toggle('bi bi-eye-slash-fill');
});

const form = document.querySelector("form");

form.addEventListener("submit",function(e){ 
    e.preventDefault();
});