package com.example.demo;
import com.example.demo.dto.CustomerDto;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.springframework.beans.factory.annotation.Autowired;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import org.springframework.http.*;
@Testcontainers
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
                properties = {"spring.profiles.active=mysql,flyway"})
class CustomerMySQLIT {
  @Container
  static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.4");
  @DynamicPropertySource
  static void props(DynamicPropertyRegistry r){
    r.add("spring.datasource.url", mysql::getJdbcUrl);
    r.add("spring.datasource.username", mysql::getUsername);
    r.add("spring.datasource.password", mysql::getPassword);
  }
  @LocalServerPort int port;
  @Autowired TestRestTemplate rest;
  @Test
  void create_and_list(){
    var dto = new CustomerDto("이몽룡","my@example.com","010");
    var base="http://localhost:"+port;
    var res = rest.postForEntity(base+"/customers", dto, String.class);
    assert(res.getStatusCode()==HttpStatus.OK);
    var list = rest.getForObject(base+"/customers", String.class);
    assert(list.contains("my@example.com"));
  }
}
