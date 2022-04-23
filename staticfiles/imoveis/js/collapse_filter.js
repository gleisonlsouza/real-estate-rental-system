'use strict'

var collapselocalizacao = document.getElementById('collapse-localizacao')
var collapsepreco = document.getElementById('collapse-preco')
var collapsetaxa = document.getElementById('collapse-taxa')
var collapsedependencia = document.getElementById('collapse-dependencia')
var collapserestricoes = document.getElementById('collapse-restricoes')
var collapseoutros = document.getElementById('collapse-outros')


collapselocalizacao.addEventListener('show.bs.collapse', function () {
    collapsepreco.classList.remove('show');
    collapsetaxa.classList.remove('show');
    collapsedependencia.classList.remove('show');
    collapserestricoes.classList.remove('show');
    collapseoutros.classList.remove('show');
});

collapsepreco.addEventListener('show.bs.collapse', function () {
    collapselocalizacao.classList.remove('show');
    collapsetaxa.classList.remove('show');
    collapsedependencia.classList.remove('show');
    collapserestricoes.classList.remove('show');
    collapseoutros.classList.remove('show');
});

collapsetaxa.addEventListener('show.bs.collapse', function () {
    collapselocalizacao.classList.remove('show');
    collapsepreco.classList.remove('show');
    collapsedependencia.classList.remove('show');
    collapserestricoes.classList.remove('show');
    collapseoutros.classList.remove('show');
});

collapsedependencia.addEventListener('show.bs.collapse', function () {
    collapselocalizacao.classList.remove('show');
    collapsepreco.classList.remove('show');
    collapsetaxa.classList.remove('show');
    collapserestricoes.classList.remove('show');
    collapseoutros.classList.remove('show');
});

collapserestricoes.addEventListener('show.bs.collapse', function () {
    collapselocalizacao.classList.remove('show');
    collapsepreco.classList.remove('show');
    collapsetaxa.classList.remove('show');
    collapsedependencia.classList.remove('show');
    collapseoutros.classList.remove('show');
});

collapseoutros.addEventListener('show.bs.collapse', function () {
    collapselocalizacao.classList.remove('show');
    collapsepreco.classList.remove('show');
    collapsetaxa.classList.remove('show');
    collapsedependencia.classList.remove('show');
    collapserestricoes.classList.remove('show');
});