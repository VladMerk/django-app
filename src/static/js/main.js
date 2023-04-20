let menus = document.querySelectorAll('#menus');

menus.forEach(function(menu){
  let currentLinks = menu.querySelectorAll('a');

  currentLinks.forEach(function(link){
    if (link.getAttribute('href') === window.location.pathname){
      link.classList.toggle('active')
      if (link.closest("ul.nested")){
        let parent = link.closest("ul.nested");
        parent.classList.toggle("active")
        console.log(parent.querySelector('.caret'));
        if (parent.querySelector(".caret")){
          parent.querySelector(".caret").classList.toggle("caret-down")
        }

      }
    }
  })
})

let toggler = document.getElementsByClassName("caret");
let i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}
