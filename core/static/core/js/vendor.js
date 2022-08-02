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

async function  btnVendor(){
document.getElementById("vendor").disabled=true;
var name = document.querySelector('#name').value;
var email = document.querySelector('#email').value;
var phonenumber = document.querySelector('#phonenumber').value;
var categories = document.querySelector('#categories').value;
var residence = document.querySelector('#residence').value;
var experience = document.querySelector('#experience').value;
var lga = document.querySelector('#lga').value;
if (name == "" || email == "" || phonenumber == "" || categories == "" || residence == "" || lga == "") {
Toast.fire({
    icon: 'error',
    title: 'Please fill all the fields'
})
document.getElementById("vendor").disabled=false;
}else {
const url ="/auth/vendor-auth"
const param = {
    name: name,
    email: email,
    phonenumber: phonenumber,
    categories: categories,
    residence: residence,
    lga: lga,
    experience: experience

}
const res=  await axios.post(url,param);
try {
    if(res.data.status=="success"){
        document.getElementById("vendor").disabled=true;
        Toast.fire({
            icon: 'success',
            title: 'Form submitted successfully, please confirm in next page '
            });
            setTimeout(() => {
            window.location.href = "/auth/vendor/confirm";
            }, 1500);
        
    }
// else if(res.data.status=="wrong"){
//         document.getElementById("vendor").disabled=false;
//         Toast.fire({
//             icon: 'error',
//             title: 'Passwords do not match'
//             }) 
// }else if(res.data.status=="exists"){
//     document.getElementById("vendor").disabled=false;
//     Toast.fire({
//         icon: 'error',
//         title: 'Username already exists'
//         })
//         }
else{
    document.getElementById("vendor").disabled=false;
    Toast.fire({
        icon: 'error',
        title: 'Something went wrong'
        })
        // calert()

    }
} catch (error) {
    console.log(error);
}
}
}
