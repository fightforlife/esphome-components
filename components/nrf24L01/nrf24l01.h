#pragma once

#include "esphome/core/component.h"
#include "esphome/components/spi/spi.h"

namespace esphome {
namespace nrf24l01 {


enum NRF24L01_PA_LEVEL { NRF24L01_PA_LEVEL_MIN = 0, NRF24L01_PA_LEVEL_LOW = 1 , NRF24L01_PA_LEVEL_HIGH = 2, NRF24L01_PA_LEVEL_MAX = 3};

enum NRF24L01_DATARATE { NRF24L01_DATARATE_1MBPS = 0, NRF24L01_DATARATE_2MBPS = 1 , NRF24L01_DATARATE_250KBPS = 2 };


class NRF24L01 : public spi::SPIDevice<spi::BIT_ORDER_MSB_FIRST, spi::CLOCK_POLARITY_LOW, spi::CLOCK_PHASE_LEADING,
                                     spi::DATA_RATE_1KHZ> {
 protected:
  InternalGPIOPin *ce_;
  NRF24L01_PA_LEVEL pa_level_;
  NRF24L01_DATARATE datarate_;
  uint8_t channel_;
  uint64_t address_;

 public:
  NRF24L01();

  void set_config_ce_pin(InternalGPIOPin *pin);
  void set_config_channel(uint8_t channel);
  void set_config_rx_address(uint64_t address);
  void set_config_pa_level(NRF24L01_PA_LEVEL pa_level);
  void set_config_datarate(NRF24L01_DATARATE datarate);

  void setup() override;
  void update() override;
  void dump_config() override;

};

}  // namespace nrf24l01
}  // namespace esphome