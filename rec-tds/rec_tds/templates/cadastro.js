const cadastro = document.getElementById('cadastro')
const nome = document.getElementById('nome')
const sobrenome = document.getElementById('sobrenome')
const email = document.getElementById('cad-email')
const senha = document.getElementById('criar-senha')
const confirmarsenha = document.getElementById('confirm-senha')
const data = document.getElementById('date')

const dataatual = new Date()
const dataISO = dataatual.toISOString().split('T')[0]

cadastro.addEventListener("submit", (event) => {
    event.preventDefault();

    checkInputNome();
    checkInputSobrenome();
    checkInputEmail();
    checkInputSenha();
})

function checkInputNome(){
    const nomevalor = nome.value;

    if(nomevalor === ""){
        erroInput(nome, "campo obrigatório!")
    }else{
        const formItem = nome.parentElement;
        formItem.className = "formulario"
    }

    console.log(nomevalor)
}

function checkInputSobrenome(){
    const sobrenomevalor = sobrenome.value;

    if(sobrenomevalor === ""){
        erroInput(sobrenome, "campo obrigatório!")
    }else{
        const formItem = sobrenome.parentElement;
        formItem.className = "formulario"
    }
}

function checkInputEmail(){
    const emailvalor = email.value;

    if(emailvalor === ""){
        erroInput(email, "campo obrigatório!")
    }else{
        const formItem = email.parentElement;
        formItem.className = "formulario"
    }
}

function checkInputSenha(){
    const senhavalor = senha.value;

    if(senhavalor === ""){
        erroInput(senha, "campo obrigatório!")
    }else if(senhavalor.length < 5){
        erroInput(senha, "senha precisa ter, no mínimo, 5 caracteres")
    }else{
        const formItem = senha.parentElement;
        formItem.className = "formulario"
    }
}



function erroInput(input, mensagem){
    const formItem = input.parentElement;
    const message = formItem.querySelector("a")

    message.innerText = mensagem;

    formItem.className = "formulario error"
}
