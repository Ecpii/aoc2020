package day4;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class second {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("./day4/filteredinput.txt"));
        ArrayList<String[]> passports = new ArrayList<>();
        HashSet<String> validEyeColors = new HashSet<>();
        {
            validEyeColors.add("amb");
            validEyeColors.add("blu");
            validEyeColors.add("brn");
            validEyeColors.add("gry");
            validEyeColors.add("grn");
            validEyeColors.add("hzl");
            validEyeColors.add("oth");
        }
        int numValidPassports = 0;

        while (in.hasNext()) {
            passports.add(in.nextLine().split(" "));
        }

        for (String[] passport : passports) {
            boolean isValidPassport = true;
            for (String field : passport) {
                String fieldName = field.substring(0, 3);
                String fieldValue = field.substring(4);

                isValidPassport = switch (fieldName) {
                    case "byr" -> {
                        try {
                            int parsedFieldValue = Integer.parseInt(fieldValue);
                            yield parsedFieldValue >= 1920 && parsedFieldValue <= 2002;
                        } catch (Exception e) {
                            yield false;
                        }
                    } case "iyr" -> {
                        try {
                            int parsedFieldValue = Integer.parseInt(fieldValue);
                            yield parsedFieldValue >= 2010 && parsedFieldValue <= 2020;
                        } catch (Exception e) {
                            yield false;
                        }
                    } case "eyr" -> {
                        try {
                            int parsedFieldValue = Integer.parseInt(fieldValue);
                            yield parsedFieldValue >= 2020 && parsedFieldValue <= 2030;
                        } catch (Exception e) {
                            yield false;
                        }
                    } case "hgt" -> {
                        try {
                            int parsedFieldValue = Integer.parseInt(fieldValue.substring(0,
                                    fieldValue.length() - 2));
                            if (fieldValue.substring(fieldValue.length() - 2).equals("cm")) {
                                yield parsedFieldValue >= 150 && parsedFieldValue <= 193;
                            }
                            yield parsedFieldValue >= 59 && parsedFieldValue <= 76;
                        } catch (Exception e) {
                            yield false;
                        }
                    } case "hcl" -> {
                        if (fieldValue.length() != 7 || fieldValue.charAt(0) != '#') {
                            yield false;
                        }
                        for (int i = 1; i < fieldValue.length(); i++) {
                            if (fieldValue.charAt(i) < 48 || fieldValue.charAt(i) > 102 ||
                                    (fieldValue.charAt(i) > 57 && fieldValue.charAt(i) < 97)) {
                                yield false;
                            }
                        }
                        yield true;
                    } case "ecl" -> {
                        if (fieldValue.length() != 3) {
                            yield false;
                        }
                        yield validEyeColors.contains(fieldValue);
                    } case "pid" -> {
                        if (fieldValue.length() != 9) {
                            yield false;
                        }
                        try {
                            Integer.parseInt(fieldValue);
                        } catch (Exception e) {
                            yield false;
                        }
                        yield true;
                    }
                    default -> true;
                };
                if (!isValidPassport) {
                    break;
                }
            }
            if (isValidPassport) {
                numValidPassports++;
            }
        }
        System.out.println(numValidPassports);
    }
}
