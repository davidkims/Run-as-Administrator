package com.example.demo.mapper;
import com.example.demo.dto.CustomerDto;
import com.example.demo.model.Customer;
import org.mapstruct.*;
@Mapper(componentModel = "spring")
public interface CustomerMapper {
  @Mapping(target="id", ignore = true)
  Customer toEntity(CustomerDto dto);
}
