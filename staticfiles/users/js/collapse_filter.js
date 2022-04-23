'use strict'

var collapsemensagens = document.getElementById('collapse_mensagens')
var collapseimoveis = document.getElementById('collapse_imoveis')
var collapsedadospessoais = document.getElementById('collapse_dados_pessoais')
var collapsedadoslogin = document.getElementById('collapse_dados_login')
var collapseoutros = document.getElementById('collapse-outros')


collapsemensagens.addEventListener('show.bs.collapse', function () {
    collapseimoveis.classList.remove('show');
    collapsedadospessoais.classList.remove('show');
    collapsedadoslogin.classList.remove('show');
});

collapseimoveis.addEventListener('show.bs.collapse', function () {
    collapsemensagens.classList.remove('show');
    collapsedadospessoais.classList.remove('show');
    collapsedadoslogin.classList.remove('show');
});

collapsedadospessoais.addEventListener('show.bs.collapse', function () {
    collapsemensagens.classList.remove('show');
    collapseimoveis.classList.remove('show');
    collapsedadoslogin.classList.remove('show');
});

collapsedadoslogin.addEventListener('show.bs.collapse', function () {
    collapsemensagens.classList.remove('show');
    collapseimoveis.classList.remove('show');
    collapsedadospessoais.classList.remove('show');
});
