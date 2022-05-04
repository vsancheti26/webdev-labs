let h_FS = 2.0;
let C_FS = 1.0;

const makeBigger = () => {
  h_FS = h_FS + 0.2;
  C_FS = C_FS + 0.2;
  document.querySelector('div.content').style.fontSize =  h_FS.toString() + 'em';
  document.querySelector('header').style.fontSize  =  C_FS.toString() + 'em';
};

const makeSmaller = () => {
  h_FS = h_FS - 0.2;
  C_FS = C_FS - 0.2;
  document.querySelector('div.content').style.fontSize =  h_FS.toString() + 'em';
  document.querySelector('header').style.fontSize  =  C_FS.toString() + 'em';
};

document.querySelector("#a1").addEventListener('click', makeBigger);
document.querySelector("#a2").addEventListener('click', makeSmaller);
