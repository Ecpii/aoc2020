package day1;

import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

class second {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("./day1/input.txt"));
        ArrayList<Integer> numbers = new ArrayList<>();

        while (in.hasNext()) {
            numbers.add(in.nextInt());
        }

        for (int i = 0; i < numbers.size() - 2; i++) {
            for (int j = i + 1; j < numbers.size() - 1; j++) {
                for (int k = j + 1; k < numbers.size(); k++) {
                    if (numbers.get(i) + numbers.get(j) + numbers.get(k) == 2020) {
                        System.out.println(numbers.get(i) * numbers.get(j) * numbers.get(k));
                        in.close();
                        break;
                    }
                }
            }
        }
    }
}
