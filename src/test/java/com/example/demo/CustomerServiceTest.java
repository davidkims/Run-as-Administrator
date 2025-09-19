package com.example.demo;
import com.example.demo.model.Customer;
import com.example.demo.repository.CustomerRepository;
import com.example.demo.service.CustomerService;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
class CustomerServiceTest {
  @Test
  void create_ok(){
    var repo = Mockito.mock(CustomerRepository.class);
    Mockito.when(repo.existsByEmail("a@b.c")).thenReturn(false);
    Mockito.when(repo.save(any(Customer.class))).thenAnswer(inv -> inv.getArgument(0));
    var svc = new CustomerService(repo);
    var saved = svc.create(new Customer(null,"A","a@b.c","010"));
    assertEquals("A", saved.getName());
  }
  @Test
  void dup_email(){
    var repo = Mockito.mock(CustomerRepository.class);
    Mockito.when(repo.existsByEmail("dup@x.com")).thenReturn(true);
    var svc = new CustomerService(repo);
    assertThrows(IllegalArgumentException.class,
      () -> svc.create(new Customer(null,"D","dup@x.com",null)));
  }
}
