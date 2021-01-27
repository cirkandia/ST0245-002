public class Punto {

    private final double x;
    private final double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double x() {
        return this.x;
    }

    public double y() {
        return this.y;
    }

    public double radioPolar() {
        return Math.sqrt((this.x * this.x) + (this.y * this.y));
    }

    public double anguloPolar() {
        return Math.atan2(this.x, this.y);
    }

    public double distanciaEuclidiana(Punto otro) {
        return Math.sqrt(Math.pow((this.x - otro.x), 2) + Math.pow((this.y - otro.y), 2));
    }
}