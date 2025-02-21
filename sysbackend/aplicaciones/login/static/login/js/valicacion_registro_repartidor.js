console.log("prueba");


document.addEventListener("DOMContentLoaded", function () {

    console.log("CARGO LA PAGINA");
    const formulario = document.getElementById('formulario');
    const divError = document.getElementById('divError');
    const mensajeError = document.getElementById('mensajeError');

    formulario.addEventListener('submit', function (evento) {
        evento.preventDefault(); // Previene el envío del formulario para poder validarlo con Javascript

       
        
        let correo = document.getElementById('id_correo').value;
        let telefono = document.getElementById('id_numero_telefono').value;
        let nombre = document.getElementById('id_nombre').value;
        let apellido = document.getElementById('id_apellido').value;
        //let tipo_vehiculo = document.getElementById('id_tipo_vehiculo').value;
        
        let password1 = document.getElementById('id_password1').value;
        let password2 = document.getElementById('id_password2').value;

        divError.classList.remove('mensajeOculto');
        // Validación de los campos
        if (correo.trim() === '') {
            mensajeError.innerText = 'El campo email no puede estar vacío.';
            return ;
        }

        if (!validarEmail(correo)) {
            mensajeError.innerText = 'El formato del email no es válido.';
            return;
        }

        if (telefono === '') {
            mensajeError.innerText = 'El campo Telefono no puede estar vacio';
            return;
        }

        if (!validarTelefono(telefono)) {
            mensajeError.innerText = 'El formato del telefono no es válido.';
            return;
        }

        if (nombre.trim() === '') {
            mensajeError.innerText = 'El campo nombre no puede estar vacío.';
            return;
        }

        if (apellido.trim() === '') {
            mensajeError.innerText = 'El campo apellido no puede estar vacío.';
            return;
        }

        if(password1 != password2){
            mensajeError.innerText = 'La contraseña no es igual, verifica por favor.';
            return;
        }


        console.log("algo parece bien...");
        // Si todo está correcto, se puede proceder a enviar el formulario o hacer alguna otra acción
        divError.classList.add('mensajeOculto');
        mensajeError.innerText = "";



        // alert('Formulario enviado con éxito!');

        //AQUI ENVIAMOS LA DATA CUANTO TODO ESTA VERIFICADO
        formulario.submit(); // Descomentar esta línea para permitir el envío del formulario
    });


    function validarEmail(email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    //Con esto validamos que el campo numero sea solo digitos
    function validarTelefono(telefono) {
        const re = /^[0-9]*$/;
        return re.test(String(telefono));
    }


});