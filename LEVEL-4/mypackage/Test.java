package mypackage;
import java.util.Random;

import org.apache.commons.lang3.*;

public class Test {
    public static void main(String[] args) {
        System.out.println(RandomStringUtils.randomAlphabetic(10));
        System.out.println(RandomStringUtils.randomNumeric(5));
        System.out.println(RandomStringUtils.random(10, true, true));
    }
}
