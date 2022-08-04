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
     document.getElementById("vendor").disabled=true;
    swal.fire({
        title: 'Verifying...',
        text: 'Please wait',
        onBeforeOpen: () => {
            Swal.showLoading()
            }

        })
        window.location.href = "/home";
    }