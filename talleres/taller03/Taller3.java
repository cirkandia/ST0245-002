public class Taller3 {

  public static void torresDeHannoi(int n) {
    torresDeHannoiAux(n, 1, 2, 3);
  }

  private static void torresDeHannoiAux(int n, int origen, int intermedio, int destino) {
    if (n == 1) {
      System.out.println("Disk 1 from " + origen + " to " + destino);
    } else {
      torresDeHannoiAux(n - 1, origen, intermedio, destino);
      System.out.println("Disk " + n + " from " + origen + " to " + destino);
      torresDeHannoiAux(n - 1, intermedio, origen, destino);
    }
  }




  public static void combinations(String s) {
    combinationsAux("", s);
  }

  private static void combinationsAux(String prefix, String s) {
    if (s.length() > 0) {
      System.out.println(prefix + s.charAt(0));
      combinationsAux(prefix + s.charAt(0), s.substring(1));
      combinationsAux(s.substring(1), prefix + s.charAt(0));
    }
  }




  public static void permutation(String str) {
    permutation("", str);
  }

  private static void permutationAux(String prefix, String str) {
    int n = str.length();
    if (n == 0)
      System.out.println(prefix);
    else {
      for (int i = 0; i < n; i++)
        permutation(prefix + str.substring(i, i++), str.substring(0, i) + str.substring(i + 1, n));
    }
  }

}