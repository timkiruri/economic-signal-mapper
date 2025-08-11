import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import TrendingUp from '@mui/icons-material/TrendingUp';
import TrendingDown from '@mui/icons-material/TrendingDown';

const EconomicIndicators = ({ forexData, commodityData }) => {
  return (
    <Card elevation={3}>
      <CardContent>
        <Typography variant="h6" gutterBottom>Market Indicators</Typography>
        <Divider sx={{ mb: 2 }} />
        
        <Grid container spacing={2}>
          {/* Forex Rates Section */}
          <Grid item xs={12}>
            <Typography variant="subtitle1" color="text.secondary">Forex Rates</Typography>
          </Grid>
          {forexData?.map((item) => (
            <Grid item xs={6} sm={4} key={item.pair}>
              <IndicatorItem 
                name={item.pair}
                value={item.rate}
                change={item.change}
              />
            </Grid>
          ))}
          
          {/* Commodities Section */}
          <Grid item xs={12} sx={{ mt: 2 }}>
            <Typography variant="subtitle1" color="text.secondary">Commodities</Typography>
          </Grid>
          {commodityData?.map((item) => (
            <Grid item xs={6} sm={4} key={item.name}>
              <IndicatorItem 
                name={item.name}
                value={item.price}
                change={item.change}
                unit={item.unit}
              />
            </Grid>
          ))}
        </Grid>
      </CardContent>
    </Card>
  );
};

const IndicatorItem = ({ name, value, change, unit }) => {
  const isPositive = change >= 0;
  
  return (
    <div>
      <Typography variant="body2" color="text.secondary">{name}</Typography>
      <Typography variant="h6">
        {value} {unit && <span style={{ fontSize: '0.8rem' }}>{unit}</span>}
      </Typography>
      <Typography 
        variant="caption" 
        color={isPositive ? 'success.main' : 'error.main'}
        sx={{ display: 'flex', alignItems: 'center' }}
      >
        {isPositive ? <TrendingUp fontSize="small" /> : <TrendingDown fontSize="small" />}
        {Math.abs(change)}%
      </Typography>
    </div>
  );
};

export default EconomicIndicators;