const toggle = document.querySelector(".toggleMenu"),
  slider = document.querySelector(".slider"),
  sidebar = document.querySelector(".sidebar"),
  icon = document.querySelector(".icon"),
  contentmenu = document.querySelectorAll(".contentMenu"),
  nama = document.querySelector(".name"),
  container = document.querySelector(".container"),
  logo = document.querySelector(".logo"),
  menu = document.querySelector(".menu"),
  menulink = document.querySelectorAll(".menu-link"),
  menulinka = document.querySelectorAll(".menu-link a"),
  iconmenu = document.querySelectorAll(".menu-link .bx"),
  appTitle = document.querySelector(".app-title");

toggle.addEventListener("click", function () {
  sidebar.classList.toggle("slide");
  sidebar.style.transform = sidebar.classList.contains("slide") ? "translateX(0)" : "translateX(-400%)";
  appTitle.classList.toggle("hidden");
  appTitle.style.opacity = appTitle.classList.contains("hidden") ? "0" : "1";
});

slider.addEventListener("click", function () {
  slider.classList.toggle("slidersmall");
  container.classList.toggle("smallcontainer");
  icon.classList.toggle("hide");
  nama.classList.toggle("hide");
  sidebar.classList.toggle("sidebarsmall");
  logo.classList.toggle("logosmall");
  menu.classList.toggle("menusmall");
  for (let i = 0; i < 7; i++) {
    menulink[i].classList.toggle("menu-link-small");
    contentmenu[i].classList.toggle("hide");
    menulinka[i].classList.toggle("menulinkasmall");
    iconmenu[i].classList.toggle("iconmenusmall");
  }
});
