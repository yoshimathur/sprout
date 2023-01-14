// Menu Clicks
const menuButton = "menu-button";
const closeButton = "menu-close-button";
const darkSplash = document.getElementById("opaque-splash");
const menuDropdown = document.getElementById("menu-dropdown");
const dropdownLink = "dropdown-nav-link";

document.getElementById(menuButton).addEventListener('click', function(event) {
  darkSplash.style.visibility = "visible";
  menuDropdown.style.visibility = "visible";
  document.body.style.overflow = "hidden";
});

document.getElementById(closeButton).addEventListener('click', function(event) {
  darkSplash.style.visibility = "collapse";
  menuDropdown.style.visibility = "collapse";
  document.body.style.overflowY = "scroll";
});

var links = document.getElementsByClassName(dropdownLink);
for (var i = 0; i < links.length; i++) {
  links[i].addEventListener('click', function(event) {
    darkSplash.style.visibility = "collapse";
    menuDropdown.style.visibility = "collapse";
    document.body.style.overflowY = "scroll";
  });
}

// Title Click
const title = "header-title";
document.getElementById(title).addEventListener('click', function(event) {
  console.log("click")
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});
