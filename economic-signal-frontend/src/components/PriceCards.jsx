import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Chip from '@mui/material/Chip';
import Box from '@mui/material/Box';
import Skeleton from '@mui/material/Skeleton';
import { useTheme } from '@mui/material/styles';
import TrendingUp from '@mui/icons-material/TrendingUp';
import TrendingDown from '@mui/icons-material/TrendingDown';

const PriceCards = ({ data, onItemSelect, selectedItem, loading }) => {
  const theme = useTheme();
  
  const formatCurrency = (value, currency) => {
    return new Intl.NumberFormat('en-KE', {
      style: 'currency',
      currency: currency || 'KES'
    }).format(value);
  };

  const getPriceChange = (item) => {
    const change = Math.random() > 0.5 ? 
      Math.random() * 5 : 
      -(Math.random() * 3);
    return {
      value: change.toFixed(1),
      isPositive: change >= 0
    };
  };

  return (
    <Box sx={{ mb: 3 }}>
      <Typography variant="h6" gutterBottom>
        Essential Commodities
      </Typography>
      <Grid container spacing={2}>
        {loading ? (
          Array.from({ length: 4 }).map((_, index) => (
            <Grid item xs={12} sm={6} md={4} key={`skeleton-${index}`}>
              <Skeleton 
                variant="rectangular" 
                height={120} 
                animation="wave"
              />
            </Grid>
          ))
        ) : (
          data.map((item) => {
            const change = getPriceChange(item);
            const isSelected = selectedItem?.id === item.id;
            
            return (
              <Grid item xs={12} sm={6} md={4} key={item.id}>
                <Card
                  onClick={() => onItemSelect(item)}
                  sx={{
                    cursor: 'pointer',
                    border: isSelected 
                      ? `2px solid ${theme.palette.primary.main}` 
                      : 'none',
                    transition: theme.transitions.create(['transform', 'box-shadow'], {
                      duration: theme.transitions.duration.short,
                    }),
                    '&:hover': {
                      transform: 'translateY(-2px)',
                      boxShadow: theme.shadows[6]
                    }
                  }}
                  elevation={isSelected ? 3 : 1}
                >
                  <CardContent>
                    <Box sx={{ 
                      display: 'flex', 
                      justifyContent: 'space-between',
                      mb: 1
                    }}>
                      <Typography 
                        variant="subtitle1" 
                        noWrap
                        sx={{ 
                          fontWeight: 600,
                          maxWidth: '70%'
                        }}
                      >
                        {item.item_name}
                      </Typography>
                      <Chip 
                        label={item.store} 
                        size="small" 
                        color="secondary"
                        sx={{ ml: 1 }}
                      />
                    </Box>

                    <Typography variant="h5" sx={{ mb: 1 }}>
                      {formatCurrency(item.price, item.currency)}
                    </Typography>

                    <Box sx={{ 
                      display: 'flex', 
                      alignItems: 'center',
                      color: change.isPositive 
                        ? theme.palette.success.main 
                        : theme.palette.error.main
                    }}>
                      {change.isPositive ? (
                        <TrendingUp fontSize="small" />
                      ) : (
                        <TrendingDown fontSize="small" />
                      )}
                      <Typography variant="caption" sx={{ ml: 0.5 }}>
                        {change.value}%
                      </Typography>
                    </Box>

                    <Typography 
                      variant="caption" 
                      color="text.secondary"
                      sx={{ 
                        display: 'block', 
                        mt: 1,
                        whiteSpace: 'nowrap',
                        overflow: 'hidden',
                        textOverflow: 'ellipsis'
                      }}
                    >
                      {item.location}
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>
            );
          })
        )}
      </Grid>
    </Box>
  );
};

export default React.memo(PriceCards);