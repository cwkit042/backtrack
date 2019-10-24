window.onload = function () {
    document.get
    Sortable.create(document.getElementById('foo'), {
        animation: 150,
    });
    container1 = document.querySelector("#container1");
    dragItem = document.querySelector("#item");
    
    container1.addEventListener("touchstart", dragStart, false);
    container1.addEventListener("touchend", dragEnd, false);
    container1.addEventListener("touchmove", drag, false);

    container1.addEventListener("mousedown", dragStart, false);
    container1.addEventListener("mouseup", dragEnd, false);
    container1.addEventListener("mousemove", drag, false);
    
    
}
var active = false;
var currentX;
var currentY;
var initialX;
var initialY;
var xOffset = 0;
var yOffset = 0;

function dragStart(e) {
    console.log(e);
  if (e.type === "touchstart") {
    if(e.target.className == "btn btn-primary"){
        console.log("click");
        e.target.click();
    }
    initialX = e.touches[0].clientX - xOffset;
    initialY = e.touches[0].clientY - yOffset;
  } else {
    initialX = e.clientX - xOffset;
    initialY = e.clientY - yOffset;
  }

  if (e.target == dragItem) {
  
    active = true;
  }
}

function dragEnd(e) {
  initialX = currentX;
  initialY = currentY;

  active = false;
}

function drag(e) {
  if (active) {
  
    e.preventDefault();
  
    if (e.type === "touchmove") {
      currentX = e.touches[0].clientX - initialX;
      currentY = e.touches[0].clientY - initialY;
    } else {
      currentX = e.clientX - initialX;
      currentY = e.clientY - initialY;
    }

    xOffset = currentX;
    yOffset = currentY;
    
    setTranslate(currentX, currentY, dragItem);
  }
}

function setTranslate(xPos, yPos, el) {
  el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}
