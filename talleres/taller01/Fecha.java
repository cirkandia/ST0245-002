public class Fecha {
    private int day;
    private int month;
    private int year;

    public Fecha(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public int dia() {
        return this.day;
    }

    public int mes() {
        return this.month;
    }

    public int anio() {
        return this.year;
    }

    public int comparar(Fecha otra) {
        if (this.year < otra.year)
            return -1;
        if (this.year > otra.year)
            return 1;

        if (this.month < otra.month)
            return -1;
        if (this.month > otra.month)
            return 1;

        if (this.day < otra.day)
            return -1;
        if (this.day > otra.day)
            return 1;

        return 0;
    }

    public String toString() {
        String texto = this.day + "/" + this.month + "/" + this.year;
        return texto;
    }
}
