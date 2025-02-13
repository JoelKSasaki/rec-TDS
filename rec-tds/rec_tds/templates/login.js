const email = document.getElementById('email')
const senha = document.getElementById('senha')

if ((email == ' ') || (senha == ' ')){
    document.getElementById("cadastrar").disabled = true
}