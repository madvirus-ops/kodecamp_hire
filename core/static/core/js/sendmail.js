
//==========default constants ==========
//axios.defaults.withCredentials = true
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
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
  
 

//=========== contact us part =========
async function  BtnContact(){
    document.getElementById("contact").disabled=true;
    var message = document.querySelector('#message').value;
    var email1 = document.querySelector('#email1').value;
    var subject = document.querySelector('#subject').value;

    if (message=="" || email1=="" || subject=="") {
      document.getElementById("contact").disabled=false;
    Toast.fire({
        icon: 'error',
        title: 'All fields are required'
      })
} else {
    const url ="/cybersafe/cal/contact"
    const param = {
    "subject": subject,
    "message":message,
    "email":email1,
    

}
  const res=  await axios.post(url,param);
   try {
    if(res.data.status=="success"){
        Toast.fire({
            icon: 'success',
            title: "message sent, we'll be in touch" 
          });
          setTimeout(() => {
            window.location.href = "/";
          }, 1500);
       
    }
    else if(res.data.status=="alreadysent"){
        document.getElementById("contact").disabled=false;
        Toast.fire({
            icon: 'error',
            title: 'message already sent'
          }) 
    }else{
        document.getElementById("contact").disabled=false;
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





// ===========subscription part===========


async function  BtnSubscribe(){
    document.getElementById("subscribe").disabled=true;
    var email1 = document.querySelector('#email1').value;

    if ( email1=="" ) {
      document.getElementById("subscribe").disabled=false;
    Toast.fire({
        icon: 'error',
        title: 'Email Required'
      })
} else {
    const url ="https://await-signup.herokuapp.com/cybersafe/cal/subscribe"
    const param = {
    "email":email1,
    

}
  const res=  await axios.post(url,param);
   try {
    if(res.data.status=="success"){
        Toast.fire({
            icon: 'success',
            title: "Subscription Added" 
          });
          setTimeout(() => {
            window.location.href = "/";
          }, 1500);
       
    }
    else if(res.data.status=="wrong"){
        document.getElementById("subscribe").disabled=false;
        Toast.fire({
            icon: 'error',
            title: 'Form not sent, try Again'
          }) 
    }else{
        document.getElementById("subscribe").disabled=false;
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