#include "esphome/core/helpers.h"
#include "esphome/core/log.h"
#include "nrf24l01.h"
#include "nrf24l01_defs.h"


#ifdef USE_ARDUINO
#include <Arduino.h>
#else  // USE_ESP_IDF
#include <driver/gpio.h>
#endif


namespace esphome {
namespace cc1101 {

static const char *const TAG = "nrf24l01";

NRF24L01::NRF24L01() {
  this->ce_ = nullptr;
  this->pa_level_ = nullptr;
  this->channel_= nullptr;
  this->datarate_= nullptr;
  this->rx_address_ = nullptr;


}

void NRF24L01::set_config_ce_pin(InternalGPIOPin *pin) { ce_ = pin; }

void NRF24L01::set_config_channel(uint8_t channel) { channel_ = channel; }

void NRF24L01::set_config_rx_address(uint64_t rx_address) { rx_address_ = rx_address; }

void NRF24L01::set_config_pa_level(NRF24L01_PA_LEVEL pa_level) { pa_level_ = pa_level; }

void NRF24L01::set_config_datarate(NRF24L01_DATARATE datarate) { datarate_ = datarate; }


void CC1101::setup() {
}

void CC1101::update() {
}

void CC1101::dump_config() {
}

}  // namespace nrf24l01
}  // namespace esphome