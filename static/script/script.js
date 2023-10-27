"use strict";
const menuIcon = document.querySelector(".menu-icon");
const sideBar = document.querySelectorAll(".sidebar-text");
const subscribed = document.querySelector(".subscribed");
const hr = document.querySelector(".hr");
const sectionSidebar = document.querySelector(".section-sidebar");
const crossIcon = document.querySelector(".cross-icon");
const sectionContent = document.querySelector(".section-content");
menuIcon.addEventListener("click", function () {
  sideBar.forEach(function (el) {
    el.classList.toggle("none");
  });
  subscribed.classList.toggle("none");
  hr.classList.toggle("hr-width");
  sectionSidebar.classList.toggle("sidebar-width");
  sectionSidebar.classList.add("menu-open");
  sectionSidebar.classList.remove("menu-close");
  sectionContent.classList.toggle("section-content-margin");
});

crossIcon.addEventListener("click", function () {
  sectionSidebar.classList.remove("menu-open");
  sectionSidebar.classList.add("menu-close");
  // sectionContent.classList.remove("section-content-margin");
});
