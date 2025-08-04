import React from 'react';
import { Box, Typography, useTheme } from '@mui/material';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const ForecastVisualization = ({ item, forecastData }) => {
  const theme = useTheme();
  
  // Transform forecast data for chart
  const chartData = forecastData.dates.map((date, index) => ({
    date,
    price: forecastData.values[index],
    currentPrice: item.price
  }));

  return (
    <Box sx={{ p: 2, border: `1px solid ${theme.palette.divider}`, borderRadius: 1 }}>
      <Typography variant="h6" gutterBottom>
        {item.item_name} Price Forecast
      </Typography>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <XAxis dataKey="date" />
          <YAxis domain={['auto', 'auto']} />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="price"
            name="Forecast"
            stroke={theme.palette.primary.main}
            strokeWidth={2}
            dot={false}
          />
          <Line
            type="monotone"
            dataKey="currentPrice"
            name="Current Price"
            stroke={theme.palette.secondary.main}
            strokeDasharray="5 5"
          />
        </LineChart>
      </ResponsiveContainer>
    </Box>
  );
};

export default ForecastVisualization;