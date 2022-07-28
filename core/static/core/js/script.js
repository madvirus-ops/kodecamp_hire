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

async function  btnLogin(){
    document.getElementById("login").disabled=true;
    var username = document.querySelector('#username').value;

var password = document.querySelector('#password').value;
if (username=="" || password=="") {
    Toast.fire({
        icon: 'error',
        title: 'Please fill all the fields'
      })
} else {
    const url ="/auth/auth"
const param = {
    "username": username,
    "password":password
}
console.log(param);
  const res=  await axios.post(url,param);
   try {
    console.log(res.data);
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