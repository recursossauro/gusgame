var TOP_LEFT   = '0';
var TOP_MIDDLE = '1';
var TOP_RIGHT  = '2';

var MIDDLE_LEFT  = '3';
var MIDDLE_RIGHT = '4';

var DOWN_LEFT   = '5';
var DOWN_MIDDLE = '6';
var DOWN_RIGHT  = '7';

var message = '';


var Letter = function(context, animation, imageLoadingListner=null, letter='@') {

  this.context = context;
  this.animation = animation;
  this.hasImageToLoad = 0;
  this.imageLoadingListner = imageLoadingListner;
  this.x = 100;
  this.y = 100;
  this.width = 30;
  this.height = 30;
  this.velX = 0;
  this.velY = 0;

}

Letter.prototype = {
  loadImage: function() {

    this.image = new Image();

    var th = this;

    this.image.onload = function() {

      // relation between image.width and image.height.
      factor = th.image.height / th.image.width;
      th.width = th.context.canvas.width/3;
      th.height = th.width * factor;
      th.x = th.context.canvas.width/2-th.width/2;
      th.y = th.context.canvas.height/2-th.height/2;
      th.isImageLoaded = 1;
      if (th.imageLoadingListner) th.imageLoadingListner.imageLoaded();

    };

    this.image.src =  this.imgUrl;
  },

  rectanglesCollision: function() {

     var rects =
     [
        {x: this.x, y: this.y, width: this.width/3, height: this.height/3}, // 0 top_left
        {x: this.x + this.width/3, y: this.y, width: this.width/3, height: this.height/3}, // 1 top_middle
        {x: this.x + this.width/3 * 2, y: this.y, width: this.width/3, height: this.height/3}, // 2 top_right

        {x: this.x, y: this.y + this.height/3, width: this.width/3, height: this.height/3}, // 3 middle_left
        {x: this.x + this.width/3 * 2, y: this.y + this.height/3, width: this.width/3, height: this.height/3}, // 4 middle_right

        {x: this.x, y: this.y + this.height/3 * 2, width: this.width/3, height: this.height/3}, // 5 down_left
        {x: this.x + this.width/3, y: this.y + this.height/3 * 2, width: this.width/3, height: this.height/3}, // 6 down_middle
        {x: this.x + this.width/3 * 2, y: this.y + this.height/3 * 2, width: this.width/3, height: this.height/3}, // 7 down_right
     ];

     return rects;
  },

  collidedWith: function(sprite, collideds) {

    if ( // TOP
        (collideds.indexOf(TOP_LEFT)   != -1) &&
        (collideds.indexOf(TOP_MIDDLE) != -1) &&
        (collideds.indexOf(TOP_RIGHT)  != -1)
      ) {
      this.velY = 100;
    } else if ( // LEFT
      (collideds.indexOf(TOP_LEFT)   != -1) &&
      (collideds.indexOf(MIDDLE_LEFT) != -1) &&
      (collideds.indexOf(MIDDLE_LEFT)  != -1)
    ) {
      this.velX = 100;
    }  else if ( // DOWN
       (collideds.indexOf(DOWN_LEFT)   != -1) &&
       (collideds.indexOf(DOWN_MIDDLE) != -1) &&
       (collideds.indexOf(DOWN_RIGHT)  != -1)
     ) {
       this.velY = -100;
     }  else if ( // RIGHTT
        (collideds.indexOf(TOP_RIGHT)   != -1) &&
        (collideds.indexOf(MIDDLE_RIGHT) != -1) &&
        (collideds.indexOf(DOWN_RIGHT)  != -1)
      ) {
        this.velX = -100;
    } else if (collideds.indexOf(TOP_LEFT) != -1) // TOP_LEFT
      {
      this.velX = 100;
      this.velY = 100;
    }  else if (collideds.indexOf(TOP_RIGHT) != -1) { //TOP_RIGHT
      this.velX = -100;
      this.velY = 100;
    }  else if (collideds.indexOf(DOWN_LEFT) != -1) { // DOWN_LEFT
      this.velX = 100;
      this.velY = -100;
    }   else if (collideds.indexOf(DOWN_RIGHT) != -1) { // DOWN_RIGHT
      this.velX = -100;
      this.velY = -100;
    }
  },

  'update': function() {

    var incrementX = this.velX * this.animation.elapsed / 1000;
    var incrementY = this.velY * this.animation.elapsed / 1000;

    this.x += incrementX;

    if (this.x < 0) {
        this.x = 0;
        this.velX = 100;
    }

    if (this.x > this.context.canvas.width - this.width) {
        this.x = this.context.canvas.width - this.width - 1;
        this.velX = -100;
    }

    this.y += incrementY;

    if (this.y < 0) {
        this.y = 0;
        this.velY = 100;
    }

    if (this.y > this.context.canvas.height - this.height) {
        this.y = this.context.canvas.height - this.height - 1;
        this.velY = -100;
    }

    // velX
    if (this.velX>0) {
      this.velX -= 2;
      if (this.velX < 0) this.velX = 0;
    }

    if (this.velX<0) {
      this.velX += 2;
      if (this.velX > 0) this.velX = 0;
    }

    // velY
    if (this.velY>0) {
      this.velY -= 2;
      if (this.velY < 0) this.velY = 0;
    }

    if (this.velY<0) {
      this.velY += 2;
      if (this.velY > 0) this.velY = 0;
    }
  },

  'draw': function() {
    this.context.fillStyle = "#000044";
    this.context.fillRect(this.x, this.y, this.width, this.height);

    // Desenhando os retângulos para visualização

    var ctx = this.context;
    var rects = this.rectanglesCollision();

    for (var i in rects) {
       ctx.save();
       ctx.strokeStyle = 'yellow';
       ctx.strokeRect(rects[i].x, rects[i].y, rects[i].width,
                      rects[i].height);
       ctx.restore();
    }

    this.context.font = "30px Arial";
    this.context.fillText(message,10,20);
  },


}
