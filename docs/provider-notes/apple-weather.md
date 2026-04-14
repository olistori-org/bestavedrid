# Apple Weather

## Access Style
API or integration layer

## Status
Not yet implemented. Access method under investigation.

## Implementation Notes

- Access depends on Apple Developer credentials and WeatherKit entitlements
- The WeatherKit REST API requires a signed JWT using an Apple Developer private key
- Integration complexity is higher than other providers
- Implement only after other providers are stable

## Required Credentials

If WeatherKit access is obtained, store credentials as GitHub Secrets:

| Secret | Description |
|---|---|
| `APPLE_WEATHER_KEY_ID` | WeatherKit key ID |
| `APPLE_WEATHER_TEAM_ID` | Apple Developer Team ID |
| `APPLE_WEATHER_APP_ID` | App bundle identifier |
| `APPLE_WEATHER_PRIVATE_KEY` | PEM-encoded private key |

## Resources

- Apple WeatherKit documentation: https://developer.apple.com/weatherkit/
- REST API requires location coordinates (lat/lon)
