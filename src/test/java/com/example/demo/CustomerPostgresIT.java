package com.example.demo;
import com.example.demo.dto.CustomerDto;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.springframework.beans.factory.annotation.Autowired;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import org.springframework.http.*;
@Testcontainers
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
                properties = {"spring.profiles.active=postgres,flyway"})
class CustomerPostgresIT {
  @Container
  static PostgreSQLContainer<?> pg = new PostgreSQLContainer<>("postgres:16");
  @DynamicPropertySource
  static void props(DynamicPropertyRegistry r){
    r.add("spring.datasource.url", pg::getJdbcUrl);
    r.add("spring.datasource.username", pg::getUsername);
    r.add("spring.datasource.password", pg::getPassword);
  }
  @LocalServerPort int port;
  @Autowired TestRestTemplate rest;
  @Test
  void create_and_list(){
    var dto = new CustomerDto("홍길동","pg@example.com","010");
    var base = "http://localhost:"+port;
    var res = rest.postForEntity(base+"/customers", dto, String.class);
    assert(res.getStatusCode()==HttpStatus.OK);
    var list = rest.getForObject(base+"/customers", String.class);
    assert(list.contains("pg@example.com"));
  }
}
