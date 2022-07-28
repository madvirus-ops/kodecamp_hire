const togglePassword = document.querySelector('#togglePassword');
  const password = document.querySelector('#exampleInputPassword1');
 //
 axios.defaults.withCredentials = true
 axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
 axios.defaults.xsrfCookieName = "csrftoken";
 const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener('mouseenter', Swal.stopTimer)
      toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })
  
 
 //
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

async function  btnsignup(){
    document.getElementById("login").disabled=true;
    var password1 = document.getElementById("exampleInputPassword1").value;
    var password2 = document.getElementById("exampleInputPassword2").value;
if (password2 != password1) {
    Toast.fire({
        icon: 'error',
        title: 'passwords do not match'
      })
} else {
    const url ="/auth/auth"
    const param = {
    "username": username,
    "password":password
}
  const res=  await axios.post(url,param);
   try {
    if(res.data.status=="success"){
        Toast.fire({
            icon: 'success',
            title: 'Login Successful, Redirecting '
          });
          setTimeout(() => {
            window.location.href = "/";
          }, 3000);
       
    }else{
        document.getElementById("login").disabled=false;
        Toast.fire({
            icon: 'error',
            title: 'invalid username or password'
          }) 
    }
   } catch (error) {
    console.log(error);
   }
}
}