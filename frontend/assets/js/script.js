const aliens = [

    {
        nome: "CHAMA",
        icone: "🔥",
        descricao: "Alienígena de energia e fogo."
    },

    {
        nome: "XLR8",
        icone: "⚡",
        descricao: "Alienígena extremamente veloz."
    },

    {
        nome: "DIAMANTE",
        icone: "💎",
        descricao: "Possui um corpo feito de cristal."
    },

    {
        nome: "QUATRO BRAÇOS",
        icone: "💪",
        descricao: "Possui enorme força física."
    },

    {
        nome: "MASSA CINZENTA",
        icone: "🧠",
        descricao: "Alienígena pequeno e extremamente inteligente."
    },

    {
        nome: "BALA DE CANHÃO",
        icone: "🟢",
        descricao: "Pode se transformar em uma esfera blindada."
    }

];


let indiceAtual = 0;


const alienName = document.getElementById("alienName");

const alienIcon = document.getElementById("alienIcon");

const alienDescription = document.getElementById("alienDescription");

const nextButton = document.getElementById("next");

const previousButton = document.getElementById("previous");

const transformButton = document.getElementById("transform");


function mostrarAlien() {

    const alien = aliens[indiceAtual];

    alienName.textContent = alien.nome;

    alienIcon.textContent = alien.icone;

    alienDescription.textContent = alien.descricao;


    alienIcon.classList.remove("change");

    void alienIcon.offsetWidth;

    alienIcon.classList.add("change");
}


nextButton.addEventListener("click", () => {

    indiceAtual++;

    if (indiceAtual >= aliens.length) {
        indiceAtual = 0;
    }

    mostrarAlien();

});


previousButton.addEventListener("click", () => {

    indiceAtual--;

    if (indiceAtual < 0) {
        indiceAtual = aliens.length - 1;
    }

    mostrarAlien();

});


transformButton.addEventListener("click", () => {

    const alien = aliens[indiceAtual];

    alert(`Transformação iniciada: ${alien.nome}`);

});