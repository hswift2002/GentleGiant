//create this class in such a way that the backgrounds are being rotated around the screen?
//maybe increasing and decreasing the intensity of the background? start w/ daytime and decrease intensity
//leading into the night and then incerasing the intensity towards daytime?
//TODO: this!!

class Background {
    constructor(w, h, animator, imageSource) {
        this.w = w;
        this.h = h;
        this.animator = animator;
        this.imageSource = imageSource;
    }

    // A method used to draw the background color,
    // and it also sets an inverse fill and stroke color,
    // used by other objects than the background.
    draw(ctx) {
        // Draw background color.
        ctx.beginPath();
        ctx.drawImage(this.animator.getImage(), 0, 0, this.w, this.h);
        ctx.closePath();
    }

    update(){
        this.animator.update();
    }

    static create(w, h, imageSource){
        const animator = Animator.create(6, 180, imageSource)
        return new Background(w, h, animator, imageSource);
    }

    
}