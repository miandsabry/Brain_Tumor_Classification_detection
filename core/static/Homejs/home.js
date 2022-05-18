let ul=document.getElementById("navbar__list");
var fragment = document.createDocumentFragment();

let sections = document.querySelectorAll("section");
let other = [...document.getElementsByClassName("new")];
console.log(other)

//for sections
sections.forEach(element => {
    let listItem = document.createElement("li");
    let link = document.createElement("a");

    link.textContent = element.id

  link.addEventListener("click", function(){
    element.scrollIntoView({
      block: 'start',
      behavior: 'smooth'
    })
})
    listItem.appendChild(link)
    fragment.appendChild(listItem)
});

//for newP&search
other.forEach(element => {
  console.log(other)
  let listItem = document.createElement("li");
  let link = document.createElement("a");
  link.textContent = element.id
  //console.log(element.id)
  listItem.appendChild(link)
  fragment.appendChild(listItem)
  if (element.id=="Search") {
    link.addEventListener("click", function()
    {
      window.location = "Search.html";
    })
  }
  if (element.id=="New Patient") {
    link.addEventListener("click", function()
    {
      window.location = "Upload.html";
    })
  }
});
ul.appendChild(fragment)

window.addEventListener("scroll", e =>
{ sections.forEach(section =>
  {const sectionTitle = section.getAttribute("data-nav");
     const rect = section.getBoundingClientRect();
     const links = document.querySelectorAll("a");
      if(rect.top >= 0 && rect.top <= 300)
      {
       section.classList.add("your-active-link");
       links.forEach(link =>
        {
          if(link.textContent === section.id){
            link.classList.add("active-link");
          }
          else{
            link.classList.remove("active-link");
          }
          })
      }
      else{
        section.classList.remove("your-active-link");
      }
  })
})

