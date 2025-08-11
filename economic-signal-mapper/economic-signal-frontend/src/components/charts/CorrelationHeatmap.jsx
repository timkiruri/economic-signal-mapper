import React from 'react';
import { Box, Typography, useTheme } from '@mui/material';
import { HeatMapGrid } from 'react-grid-heatmap';

const CorrelationHeatmap = ({ item, correlations }) => {
  const theme = useTheme();
  
  // Prepare data for heatmap
  const labels = Object.keys(correlations);
  const values = labels.map(key => correlations[key]);
  
  const data = [
    values // Single row for this visualization
  ];

  return (
    <Box sx={{ p: 2, border: `1px solid ${theme.palette.divider}`, borderRadius: 1 }}>
      <Typography variant="h6" gutterBottom>
        {item.item_name} Price Correlations
      </Typography>
      <HeatMapGrid
        data={data}
        xLabels={labels}
        yLabels={['']}
        xLabelsStyle={() => ({
          fontSize: '0.8rem',
          color: theme.palette.text.secondary
        })}
        cellStyle={(_x, _y, ratio) => ({
          background: `rgb(63, 81, 181, ${Math.abs(ratio)})`,
          fontSize: '0.8rem',
          color: ratio > 0.5 ? '#fff' : theme.palette.text.primary
        })}
        cellHeight="2rem"
        xLabelsPos="bottom"
        onClick={(x, y) => console.log(`Clicked ${labels[x]} (${data[y][x]})`)}
      />
    </Box>
  );
};

export default CorrelationHeatmap;