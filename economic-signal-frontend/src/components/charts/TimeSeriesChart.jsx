import React from 'react';
import { Box, Typography, useTheme } from '@mui/material';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const TimeSeriesChart = ({ item, prices }) => {
  const theme = useTheme();
  
  // Transform price history for chart
  const chartData = prices.map(price => ({
    date: new Date(price.timestamp).toLocaleDateString(),
    price: price.price,
    store: price.store
  }));

  return (
    <Box sx={{ p: 2, border: `1px solid ${theme.palette.divider}`, borderRadius: 1 }}>
      <Typography variant="h6" gutterBottom>
        {item.item_name} Price History
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
            name={`Price (${item.currency})`}
            stroke={theme.palette.primary.main}
            strokeWidth={2}
            activeDot={{ r: 6 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </Box>
  );
};

export default TimeSeriesChart;