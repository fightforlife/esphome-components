import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation, pins
from esphome.components import spi
from esphome.const import CONF_ID

DEPENDENCIES = ["spi"]
CODEOWNERS = ["@fightforlife"]
nrf24l01_ns = cg.esphome_ns.namespace("nrf24l01")
NRF24L01 = ns.class_("NRF24L01", spi.SPIDevice)


CONF_NRF24L01_ID = "nrf24l01_id"
CONF_NRF24L01_CE_PIN = "ce_pin"
CONF_NRF24L01_CHANNEL = "channel"
CONF_NRF24L01_RX_ADDRESS = "rx_address"


CONF_NRF24L01_PA_LEVEL = "pa_level"
NRF24L01_PA_LEVEL = nrf24l01_ns.enum("NRF24L01_PA_LEVEL")
NRF24L01_PA_LEVEL = {
    "min": NRF24L01_PA_LEVEL.NRF24L01_PA_LEVEL_MIN,
    "low": NRF24L01_PA_LEVEL.NRF24L01_PA_LEVEL_LOW,
    "high": NRF24L01_PA_LEVEL.NRF24L01_PA_LEVEL_HIGH,
    "max": NRF24L01_PA_LEVEL.NRF24L01_PA_LEVEL_MAX,
}

CONF_NRF24L01_DATARATE = "datarate"
NRF24L01_DATARATE = nrf24l01_ns.enum("NRF24L01_DATARATE")
NRF24L01_DATARATE = {
    "1mbps": NRF24L01_DATARATE.NRF24L01_DATARATE_1MBPS,
    "2mbps": NRF24L01_DATARATE.NRF24L01_DATARATE_2MBPS,
    "250kbps": NRF24L01_DATARATE.NRF24L01_DATARATE_250KBPS,
}


def validate_rx_adress(value):
    if(len(value) < 3 and len(value) > 5:
        raise cv.Invalid("only 3-5 bytes are possible")
    return value


CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(NRF24L01),
            cv.Required(CONF_CE_PIN): pins.gpio_output_pin_schema,
            cv.Optional(CONF_NRF24L01_PA_LEVEL, default="max"): cv.enum(NRF24L01_PA_LEVEL),
            cv.Optional(CONF_NRF24L01_CHANNEL, default=76): cv.int_range(min=0, max=125),
            cv.Optional(CONF_NRF24L01_DATARATE, default="1mbps"): cv.enum(NRF24L01_DATARATE),
            cv.Required(CONF_NRF24L01_RX_ADDRESS, default="NRF24"): cv.All(string_strict, validate_rx_adress)
        }
    .extend(spi.spi_device_schema(cs_pin_required=True))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await spi.register_spi_device(var, config)

    ce_pin = await cg.gpio_pin_expression(config[CONF_NRF24L01_CE_PIN])
    cg.add(var.set_config_ce_pin(ce_pin))

    cg.add(var.set_config_channel(config[CONF_NRF24L01_CHANNEL]))
    cg.add(var.set_config_rx_address(config[CONF_NRF24L01_RX_ADDRESS]))  
    cg.add(var.set_config_pa_level(config[CONF_NRF24L01_PA_LEVEL]))
    cg.add(var.set_config_datarate(config[CONF_NRF24L01_DATARATE]))   