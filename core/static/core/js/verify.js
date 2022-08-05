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

function  btnVerify(){
    try {
     document.getElementById("vendor").disabled=true;
     Toast.fire({
        icon: 'success',
        title: 'Verifying...'
      });
      setTimeout(() => {
        window.location.href = "/home";
      }, 1500);
    }
    catch(err){
        console.log(err);
    }
}