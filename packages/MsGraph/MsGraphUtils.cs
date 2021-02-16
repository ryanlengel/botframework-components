namespace Microsoft.Bot.Component.MsGraph
{
    using System;
    using System.Runtime.InteropServices;
    using AdaptiveExpressions;

    public class MsGraphUtils
    {
        public static TimeZoneInfo ConvertTimeZoneFormat(string timezone)
        {
            TimeZoneInfo convertedTimeZone = null;
            string convertedTimeZoneStr;

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                convertedTimeZoneStr = TimeZoneConverter.IanaToWindows(timezone);
            }
            else
            {
                convertedTimeZoneStr = TimeZoneConverter.WindowsToIana(timezone);
            }

            try
            {
                convertedTimeZone = TimeZoneInfo.FindSystemTimeZoneById(convertedTimeZoneStr);
            }
            catch
            {
                throw new Exception($"{timezone} is an illegal timezone");
            }

            return convertedTimeZone;
        }
    }
}
