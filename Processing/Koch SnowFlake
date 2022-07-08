int order;

void setup(){
  background(255);
  size(400, 400);
  order = 3;
  drawSnowFlakeWithOrder(order); 
}

void draw() {
}

void mousePressed(){ 
  background(255);
  order = (int) map(mouseY, 0, width, 0, 7);
  drawSnowFlakeWithOrder(order);
}

void drawSnowFlakeWithOrder(int order){
  
  int side = (int) (min(width, height) * 0.8);
  int triangleHeight = (int) (side * Math.sin(Math.toRadians(60.0)));
  
  Point p1 = new Point(width / 2, 10);
  Point p2 = new Point(width / 2 - side / 2, 10 + triangleHeight);
  Point p3 = new Point(width / 2 + side / 2, 10 + triangleHeight);
  
  int r = (int) map(order, 0, 7, 0, 255);
  int g = (int) map(mouseX, 0, width, 0, 255);
  int b = (int) map(mouseY, 0, height, 0, 255);

  drawSnowFlake(order, p1, p2, 1, r, g, b);
  drawSnowFlake(order, p2, p3, 1, r, g, b);
  drawSnowFlake(order, p3, p1, 1, r, g, b);
}

class Point {
  int x;
  int y;
 
  Point(int xp, int yp){
    x = xp;
    y = yp;
  } 
   
  void draw(int weight, int r, int g, int b){
    strokeWeight(weight);
    stroke(r, g, b);
    point(x,y);
  }  
}

void drawSnowFlake(int order, Point p1, Point p2, int weight, int r, int g, int b) {
  
  if (order == 0) {
    strokeWeight(weight);
    stroke(r,g,b);
    line(p1.x, p1.y, p2.x, p2.y);
  } else {
    int deltaX = p2.x - p1.x;
    int deltaY = p2.y - p1.y;
    
    double cosConst = Math.cos(Math.toRadians(30.0));
    int zx = (int)((p1.x + p2.x)/2 + cosConst * (p1.y - p2.y)/3.0);
    int zy = (int)((p1.y + p2.y)/2 + cosConst * (p2.x - p1.x)/3.0);
    
    Point x = new Point(p1.x + deltaX / 3, p1.y + deltaY / 3);
    Point y = new Point(p1.x + deltaX * 2 / 3, p1.y + deltaY * 2 / 3);
    Point z = new Point(zx, zy);

    drawSnowFlake(order - 1, p1, x, 1 , r, g, b);
    drawSnowFlake(order - 1, x, z, 1 , r, g, b);
    drawSnowFlake(order - 1, z, y, 1 , r, g, b);
    drawSnowFlake(order - 1, y, p2, 1 , r, g, b);
  }
  
}
