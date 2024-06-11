#!/usr/bin/env python3
from cereal import car
from openpilot.common.conversions import Conversions as CV
<<<<<<< HEAD
from openpilot.selfdrive.car.mazda.values import CAR, LKAS_LIMITS
from openpilot.selfdrive.car import create_button_events, get_safety_config
=======
from openpilot.selfdrive.car.mazda.values import CAR, LKAS_LIMITS, BUTTON_STATES
from openpilot.selfdrive.car import create_button_events, get_safety_config, create_mads_event
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)
from openpilot.selfdrive.car.interfaces import CarInterfaceBase

ButtonType = car.CarState.ButtonEvent.Type
EventName = car.CarEvent.EventName
GearShifter = car.CarState.GearShifter

class CarInterface(CarInterfaceBase):
  def __init__(self, CP, CarController, CarState):
    super().__init__(CP, CarController, CarState)
<<<<<<< HEAD
=======
    self.buttonStatesPrev = BUTTON_STATES.copy()
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)

  @staticmethod
  def _get_params(ret, candidate, fingerprint, car_fw, experimental_long, docs):
    ret.carName = "mazda"
    ret.safetyConfigs = [get_safety_config(car.CarParams.SafetyModel.mazda)]
    ret.radarUnavailable = True
    ret.customStockLongAvailable = True

    ret.dashcamOnly = candidate not in (CAR.MAZDA_CX5_2022, CAR.MAZDA_CX9_2021)

    ret.steerActuatorDelay = 0.1
    ret.steerLimitTimer = 0.8

    CarInterfaceBase.configure_torque_tune(candidate, ret.lateralTuning)

    if candidate not in (CAR.MAZDA_CX5_2022, ):
      ret.minSteerSpeed = LKAS_LIMITS.DISABLE_SPEED * CV.KPH_TO_MS

    ret.centerToFront = ret.wheelbase * 0.41

    return ret

  # returns a car.CarState
  def _update(self, c):
    ret = self.CS.update(self.cp, self.cp_cam)
<<<<<<< HEAD

    # TODO: add button types for inc and dec
    self.CS.button_events = [
      *self.CS.button_events,
      *create_button_events(self.CS.distance_button, self.CS.prev_distance_button, {1: ButtonType.gapAdjustCruise}),
      *create_button_events(self.CS.lkas_enabled, self.CS.prev_lkas_enabled, {1: ButtonType.altButton1}),
    ]

    self.CS.mads_enabled = self.get_sp_cruise_main_state(ret)

    self.CS.accEnabled = self.get_sp_v_cruise_non_pcm_state(ret, c.vCruise, self.CS.accEnabled)
=======
    self.sp_update_params()

    # TODO: add button types for inc and dec
    buttonEvents = create_button_events(self.CS.distance_button, self.CS.prev_distance_button, {1: ButtonType.gapAdjustCruise})

    for button in self.CS.buttonStates:
      if self.CS.buttonStates[button] != self.buttonStatesPrev[button]:
        be = car.CarState.ButtonEvent.new_message()
        be.type = button
        be.pressed = self.CS.buttonStates[button]
        buttonEvents.append(be)

    self.CS.mads_enabled = self.get_sp_cruise_main_state(ret, self.CS)

    self.CS.accEnabled = self.get_sp_v_cruise_non_pcm_state(ret, self.CS.accEnabled,
                                                            buttonEvents, c.vCruise)
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)

    if ret.cruiseState.available:
      if self.enable_mads:
        if not self.CS.prev_mads_enabled and self.CS.mads_enabled:
          self.CS.madsEnabled = True
<<<<<<< HEAD
        if any(b.type == ButtonType.altButton1 and b.pressed for b in self.CS.button_events):
          self.CS.madsEnabled = not self.CS.madsEnabled
        self.CS.madsEnabled = self.get_acc_mads(ret, self.CS.madsEnabled)
=======
        if self.CS.prev_lkas_enabled != self.CS.lkas_enabled:
          self.CS.madsEnabled = not self.CS.madsEnabled
        self.CS.madsEnabled = self.get_acc_mads(ret.cruiseState.enabled, self.CS.accEnabled, self.CS.madsEnabled)
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)
    else:
      self.CS.madsEnabled = False

    if not self.CP.pcmCruise or (self.CP.pcmCruise and self.CP.minEnableSpeed > 0) or not self.CP.pcmCruiseSpeed:
<<<<<<< HEAD
      if any(b.type == ButtonType.cancel for b in self.CS.button_events):
        self.get_sp_cancel_cruise_state()
    if self.get_sp_pedal_disengage(ret):
      self.get_sp_cancel_cruise_state()
      ret.cruiseState.enabled = ret.cruiseState.enabled if not self.enable_mads else False if self.CP.pcmCruise else self.CS.accEnabled
=======
      if any(b.type == ButtonType.cancel for b in buttonEvents):
        self.CS.madsEnabled, self.CS.accEnabled = self.get_sp_cancel_cruise_state(self.CS.madsEnabled)
    if self.get_sp_pedal_disengage(ret):
      self.CS.madsEnabled, self.CS.accEnabled = self.get_sp_cancel_cruise_state(self.CS.madsEnabled)
      ret.cruiseState.enabled = False if self.CP.pcmCruise else self.CS.accEnabled
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)

    if self.CP.pcmCruise and self.CP.minEnableSpeed > 0 and self.CP.pcmCruiseSpeed:
      if ret.gasPressed and not ret.cruiseState.enabled:
        self.CS.accEnabled = False
      self.CS.accEnabled = ret.cruiseState.enabled or self.CS.accEnabled

<<<<<<< HEAD
    ret = self.get_sp_common_state(ret)

    ret.buttonEvents = [
      *self.CS.button_events,
      *self.button_events.create_mads_event(self.CS.madsEnabled, self.CS.out.madsEnabled)  # MADS BUTTON
    ]
=======
    ret, self.CS = self.get_sp_common_state(ret, self.CS, gap_button=bool(self.CS.distance_button))

    # MADS BUTTON
    if self.CS.out.madsEnabled != self.CS.madsEnabled:
      if self.mads_event_lock:
        buttonEvents.append(create_mads_event(self.mads_event_lock))
        self.mads_event_lock = False
    else:
      if not self.mads_event_lock:
        buttonEvents.append(create_mads_event(self.mads_event_lock))
        self.mads_event_lock = True

    ret.buttonEvents = buttonEvents
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)

    # events
    events = self.create_common_events(ret, c, extra_gears=[GearShifter.sport, GearShifter.low, GearShifter.brake],
                                       pcm_enable=False)

<<<<<<< HEAD
    events, ret = self.create_sp_events(ret, events)
=======
    events, ret = self.create_sp_events(self.CS, ret, events)
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)

    #if self.CS.lkas_disabled:
    #  events.add(EventName.lkasDisabled)
    if self.CS.low_speed_alert:
      events.add(EventName.belowSteerSpeed)

<<<<<<< HEAD
    ret.customStockLong = self.update_custom_stock_long()

    ret.events = events.to_msg()

=======
    ret.customStockLong = self.CS.update_custom_stock_long(self.CC.cruise_button, self.CC.final_speed_kph,
                                                           self.CC.target_speed, self.CC.v_set_dis,
                                                           self.CC.speed_diff, self.CC.button_type)

    ret.events = events.to_msg()

    self.buttonStatesPrev = self.CS.buttonStates.copy()

>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)
    return ret
