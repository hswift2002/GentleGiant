class Castle {
    constructor(position, w, h, animator) {
        this.position = position;
        this.w = w;
        this.h = h;
        this.animator = animator;
    }

    // A method that can be used to draw the castle.
    draw(ctx) {
        ctx.beginPath();
        ctx.drawImage(this.animator.getImage(), this.position.x, this.position.y, this.w, this.h);
        ctx.closePath();
    }

    // A method that can be used to create a castle
    // without passing a point2D.
    static create(x, y, w, h, imageSource) {
        const position = new Point2D(x, y);
        const animator = Animator.create(2, 5, imageSource);
        return new Castle(position, w, h, animator);
    }
}