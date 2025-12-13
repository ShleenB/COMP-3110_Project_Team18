interface SmartHomeSystem_mut {

    void turnOnDevice(String deviceId);
    void turnOffDevice(String deviceId);
    void toggleDevice(String deviceId);
    boolean isDeviceOn(String deviceId);

    public void renameDevice(String deviceId, String newName);
    void assignDeviceToRoom(String deviceId, String roomName);
    String getDeviceRoom(String deviceId);
    String getDeviceName(String deviceId);

    void setThermostatTemperature(double celsius);
    double getThermostatTemperature();
    public void setLightBrightness(String deviceId, int percent);
    int getLightBrightness(String deviceId);

    void scheduleOn(String deviceId, String time24h);
    void scheduleOff(String deviceId, String time24h);
    void cancelSchedule(String deviceId);

    //the home is now too smart
    String getLastAlertMessage();
}
