// const togglePassword = document.querySelector('#togglePassword');
//   const password = document.querySelector('#exampleInputPassword1');
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
//   togglePassword.addEventListener('click', function (e) {
//     const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
//     password.setAttribute('type', type);
//     this.classList.toggle('bi bi-eye-slash-fill');
// });
// const togglePassword2 = document.querySelector('#togglePassword2');
// const passwordSecond = document.querySelector('#exampleInputPassword2');

// togglePassword2.addEventListener('click', function (e) {
//     const type = passwordSecond.getAttribute('type') === 'password' ? 'text' : 'password';
//     passwordSecond.setAttribute('type', type);
//     this.classList.toggle('bi bi-eye-slash-fill');
// });

// const form = document.querySelector("form");

// form.addEventListener("submit",function(e){ 
//     e.preventDefault();
// });

async function  btnSignup(){
    document.getElementById("signup").disabled=true;
    var username = document.querySelector('#username').value;
    var email = document.querySelector('#email').value;
    var password1 = document.querySelector('#password1').value;
    var password2 = document.querySelector('#password2').value;
    var check = document.querySelector('#check').value;
    if (password1=="" || password2=="" || username=="" || email=="" || check=="") {
    Toast.fire({
        icon: 'error',
        title: 'All fields are required'
      })
} else {
    const url ="/auth/authup"
    const param = {
    "username": username,
    "password1":password1,
    "email":email,
    "check":check,
    "password2":password2

}
  const res=  await axios.post(url,param);
   try {
    if(res.data.status=="success"){
        Toast.fire({
            icon: 'success',
            title: 'Signup successful, Redirecting to login'
          });
          setTimeout(() => {
            window.location.href = "/auth/signin";
          }, 1500);
       
    }
    else if(res.data.status=="wrong"){
        document.getElementById("signup").disabled=false;
        Toast.fire({
            icon: 'error',
            title: 'Passwords do not match'
          }) 
    }else if(res.data.status=="exists"){
        document.getElementById("signup").disabled=false;
        Toast.fire({
            icon: 'error',
            title: 'Username already exists'
          })
         }else{
        document.getElementById("signup").disabled=false;
        Toast.fire({
            icon: 'error',
            title: 'Something went wrong'
          })

      }
   } catch (error) {
    console.log(error);
   }
}
}
