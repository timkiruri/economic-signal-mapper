import React, { useState, useEffect } from 'react';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/material/Alert';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';

// Component imports
import PriceCards from "../PriceCards";
import EconomicIndicators from "../EconomicIndicators";
import RegionalMap from "../RegionalMap"; 
import AlertsPanel from "../AlertsPanel";
import TimeSeriesChart from "../charts/TimeSeriesChart";
import ForecastVisualization from "../charts/ForecastVisualization";
import CorrelationHeatmap from "../charts/CorrelationHeatmap";

// Mock API service
const mockAPI = {
  getPrices: async () => [
    { 
      id: 1, 
      item_name: "Maize Flour 2kg", 
      price: 180, 
      currency: "KES", 
      store: "Naivas", 
      location: "Nairobi",
      timestamp: new Date().toISOString()
    },
    { 
      id: 2, 
      item_name: "Petrol (1L)", 
      price: 150, 
      currency: "KES", 
      store: "Shell", 
      location: "Nairobi",
      timestamp: new Date().toISOString()
    }
  ],
  getForex: async () => [
    { pair: 'USD/KES', rate: 150.25, change: 0.52 },
    { pair: 'EUR/KES', rate: 165.80, change: -0.31 }
  ],
  getCommodities: async () => [
    { name: 'Brent Crude', price: 85.60, unit: 'USD/barrel', change: 1.2 },
    { name: 'Wheat', price: 320.00, unit: 'USD/ton', change: -5.0 }
  ],
  getAlerts: async () => [
    {
      id: 1,
      item: "Maize Flour",
      message: "Price spike detected (15% increase)",
      severity: "High",
      timestamp: new Date(Date.now() - 3600000)
    }
  ],
  getRegionalData: async () => [
    {
      id: 1,
      name: "Nairobi",
      lat: -1.286389,
      lng: 36.817223,
      avgPrice: 185.50
    }
  ]
};

const Dashboard = () => {
  const [state, setState] = useState({
    prices: [],
    forexData: [],
    commodityData: [],
    priceAlerts: [],
    regionalPrices: [],
    selectedItem: null,
    loading: true,
    error: null
  });

  useEffect(() => {
    const loadData = async () => {
      try {
        const [prices, forexData, commodityData, priceAlerts, regionalPrices] = 
          await Promise.all([
            mockAPI.getPrices(),
            mockAPI.getForex(),
            mockAPI.getCommodities(),
            mockAPI.getAlerts(),
            mockAPI.getRegionalData()
          ]);

        setState(prev => ({
          ...prev,
          prices,
          forexData,
          commodityData,
          priceAlerts,
          regionalPrices,
          loading: false
        }));

      } catch (err) {
        console.error("API Error:", err);
        setState(prev => ({
          ...prev,
          error: "Failed to load dashboard data",
          loading: false
        }));
      }
    };

    loadData();
  }, []);

  const handleDismissAlert = (id) => {
    setState(prev => ({
      ...prev,
      priceAlerts: prev.priceAlerts.filter(alert => alert.id !== id)
    }));
  };

  const handleItemSelect = (item) => {
    setState(prev => ({ ...prev, selectedItem: item }));
  };

  const handleRegionSelect = (regionId) => {
    console.log("Selected region:", regionId);
  };

  const { 
    prices, 
    forexData, 
    commodityData, 
    priceAlerts, 
    regionalPrices, 
    selectedItem, 
    loading, 
    error 
  } = state;

  return (
    <>
      <CssBaseline />
      <Container maxWidth="xl" sx={{ py: 3 }}>
        <Typography variant="h4" component="h1" gutterBottom sx={{ mb: 4 }}>
          Economic Signal Mapper
        </Typography>

        {loading ? (
          <Box display="flex" justifyContent="center" py={10}>
            <CircularProgress size={60} />
          </Box>
        ) : error ? (
          <Alert severity="error" sx={{ mb: 3 }}>
            {error}
          </Alert>
        ) : (
          <>
            <Grid container spacing={3} sx={{ mb: 3 }}>
              <Grid item xs={12} md={6}>
                <PriceCards 
                  data={prices} 
                  onItemSelect={handleItemSelect}
                  selectedItem={selectedItem}
                />
              </Grid>
              <Grid item xs={12} md={6}>
                <EconomicIndicators 
                  forexData={forexData} 
                  commodityData={commodityData} 
                />
              </Grid>
            </Grid>

            <Grid container spacing={3} sx={{ mb: 3 }}>
              <Grid item xs={12} md={8}>
                <RegionalMap 
                  regionalPrices={regionalPrices} 
                  onRegionSelect={handleRegionSelect} 
                />
              </Grid>
              <Grid item xs={12} md={4}>
                <AlertsPanel 
                  alerts={priceAlerts} 
                  onDismiss={handleDismissAlert} 
                />
              </Grid>
            </Grid>

            {selectedItem && (
              <>
                <Grid container spacing={3} sx={{ mb: 3 }}>
                  <Grid item xs={12} lg={6}>
                    <TimeSeriesChart 
                      item={selectedItem} 
                      historicalData={prices.filter(p => p.id === selectedItem.id)} 
                    />
                  </Grid>
                  <Grid item xs={12} lg={6}>
                    <ForecastVisualization 
                      item={selectedItem}
                      forecastData={{
                        dates: ['Jan', 'Feb', 'Mar'],
                        values: [selectedItem.price, selectedItem.price * 1.05, selectedItem.price * 1.1]
                      }}
                    />
                  </Grid>
                </Grid>
                <Grid item xs={12}>
                  <CorrelationHeatmap 
                    item={selectedItem}
                    correlations={{
                      "USD/KES": 0.76,
                      "Fuel Price": -0.32
                    }}
                  />
                </Grid>
              </>
            )}
          </>
        )}

        <Snackbar
          open={!!error}
          autoHideDuration={6000}
          onClose={() => setState(prev => ({ ...prev, error: null }))}
          anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
        >
          <Alert severity="error">
            {error}
          </Alert>
        </Snackbar>
      </Container>
    </>
  );
};

export default Dashboard;