var gallery = {
  cnt: 0,
  container: document.getElementById("container_image"),
  timer: null,
  rds: "btn1",
  pos: 0,
  top: 1,
  init: function(i) {
    this.cnt = i;
    this.container.style.width = i * 700 + "px";
    this.timer = setInterval(function() {
      gallery.start();
    }, 1500);
  },
  start: function() {
    if (this.top == 1) {
      this.pos = 0;
      this.top += 1;
      document.getElementById("btn1").style.backgroundColor = "red";
      document.getElementById("btn2").style.backgroundColor = "green";
      document.getElementById("btn3").style.backgroundColor = "green";
    } else if (this.top == 2) {
      this.pos -= 350 * 2;
      this.top += 1;
      document.getElementById("btn1").style.backgroundColor = "green";
      document.getElementById("btn2").style.backgroundColor = "red";
      document.getElementById("btn3").style.backgroundColor = "green";
    } else if (this.top == 3) {
      this.pos -= 350 * 2;
      this.top = 1;
      document.getElementById("btn1").style.backgroundColor = "green";
      document.getElementById("btn2").style.backgroundColor = "green";
      document.getElementById("btn3").style.backgroundColor = "red";
    }
    this.container.style.left = this.pos + "px";
  },
  slide: function(event) {
    var e = event || window.event;
    var target = e.target;

    if (target.tagName.toLowerCase() != "span") return;

    var id_click = target.id;
    var pos = document.getElementById(id_click).offsetLeft;
    if (id_click == "btn1") pos = 0;
    else if (id_click == "btn2") pos -= 526 * 2;
    else if (id_click == "btn3") pos -= 593 * 3;
    else pos = 247;
    this.container.style.left = pos + "px";
  }
}