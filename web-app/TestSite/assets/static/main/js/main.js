var navMenu = document.querySelector("#menu-icon");
var sidePanel = document.querySelector(".side-panel");
var search = document.querySelector(".btn-search");
var comments = document.querySelector(".comments");
var sidePanelComments = document.querySelector(".side-panel-comments");
var xmarkComments = document.querySelector(".xmark");
var formComment = document.querySelector("#id_comment");
var stateMain = document.querySelector(".states_main");


if (formComment){
    formComment.addEventListener("click", function() {
        formComment.style.height = "200px";
    });

    xmarkComments.addEventListener("click", function() {
        formComment.style.height = "50px";
        sidePanelComments.classList.toggle('comments-active');
        if (sidePanelComments.classList.contains('comments-active')) {
            sidePanelComments.style.right = '0px';
        } else {
            sidePanelComments.style.right = '-520px';
        }
    });


}


if (comments){
    comments.addEventListener("click", function() {
        sidePanelComments.classList.toggle('comments-active');
        if (sidePanelComments.classList.contains('comments-active')) {
            sidePanelComments.style.right = '0px';
        } else {
            sidePanelComments.style.right = '-100%';
            formComment.style.height = "50px";
        }
    });
}


navMenu.addEventListener("click", function() {
    sidePanel.classList.toggle('active');
    if (sidePanel.classList.contains('active')) {
      sidePanel.style.left = '0';
    } else {
        sidePanel.style.left = '-100%';
    }
});

search.addEventListener("mouseover", function() {
    if (document.documentElement.clientWidth <= 820){
        var searchInput = document.querySelector("#search-input");

        searchInput.style.display = 'block';

    }

});

function func(a){
    var b = a + a;
    return b + a;
};

alert(func(5));