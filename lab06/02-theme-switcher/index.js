const makedesert = () => {
    document.querySelector('body').className = 'desert'
};

const makeocean = () => {
  document.querySelector('body').className = 'ocean'
};

const makehighcontrast = () => {
    document.querySelector('body').className = 'high-contrast'
};

const makedefault = () => {
    document.querySelector('body').className = ''
};

document.querySelector("#default").addEventListener('click', makedefault);
document.querySelector("#desert").addEventListener('click', makedesert);
document.querySelector("#ocean").addEventListener('click', makeocean);
document.querySelector("#high-contrast").addEventListener('click', makehighcontrast);
